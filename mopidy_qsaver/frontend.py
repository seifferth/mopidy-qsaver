from __future__ import unicode_literals

import logging

import os.path

from mopidy.core import CoreListener

import pykka
import json

logger = logging.getLogger(__name__)


class QSaverFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(QSaverFrontend, self).__init__()
        self.config = config
        self.core = core
        self.backup_file = self.config.get('qsaver')['backup_file']
        self.is_playing = False

    def saveQueue(self):
        logger.info("Qsaver is saving your tracklist")
        with open(self.backup_file, 'w') as f:
            tracklist = self.core.tracklist
            state_playing = self.is_playing
            playing = self.core.playback.get_current_tl_track().get()
            playing_id = playing.tlid if playing is not None else None
            json.dump(
                {
                  "uris": [t.uri for t in tracklist.get_tracks().get()],
                  "consume": tracklist.get_consume().get(),
                  "random": tracklist.get_random().get(),
                  "repeat": tracklist.get_repeat().get(),
                  "single": tracklist.get_single().get(),
                  "track": playing_id,
                  "playing": state_playing,
                },
                f,
                indent=2,
            )
        f.closed
        logger.info("Qsaver has saved your tracklist!")

    def restoreQueue(self):
        logger.info("Qsaver is restoring your tracklist")
        try:
            with open(self.backup_file, 'r') as f:
                old_state = json.load(f)
                tracklist = self.core.tracklist
                tracklist.add(uris=old_state.get("uris", list()))
                tracklist.set_consume(old_state.get("consume", False))
                tracklist.set_random(old_state.get("random", False))
                tracklist.set_repeat(old_state.get("repeat", False))
                tracklist.set_single(old_state.get("single", False))
                track = old_state.get("track", None)
                playing = old_state.get("playing", False)
                if track and playing:
                    # FIXME no way to just move to the track without playing it
                    self.core.playback.play(tlid=track)
            f.closed
            logger.info("Qsaver has restored your tracklist!")
        except json.decoder.JSONDecodeError as e:
            logger.info(
                "Qsaver was unable to load the saved state, sorry. " +
                "Looks like it contains broken json."
            )
        except Exception:
            logger.info("Qsaver unable to restore tracklist file")

    def on_start(self):
        self.restoreQueue()

    def on_stop(self):
        self.saveQueue()

    def tracklist_changed(self):
        self.saveQueue()

    def track_playback_paused(self, tl_track, time_position):
        self.is_playing = False

    def track_playback_started(self, tl_track):
        self.is_playing = True

    def track_playback_resumed(self, tl_track, time_position):
        self.is_playing = True

    def getUri(track):
        return track.uri
