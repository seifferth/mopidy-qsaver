from __future__ import unicode_literals

import logging

from mopidy.core import CoreListener

import pykka

logger = logging.getLogger(__name__)


class QSaverFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(QSaverFrontend, self).__init__()
        self.config = config
        self.core = core

    def saveQueue(self):
        # TODO: save the queue to a local file
        logger.info("Qsaver is saving the tracklist")

    def restoreQueue(self):
        # TODO: restore the queue from a local file
        logger.info("Qsaver is restoring your tracklist")

    def on_start(self):
        self.restoreQueue()

    def on_stop(self):
        self.saveQueue()

    def track_playback_started(self, tl_track):
        self.saveQueue()
