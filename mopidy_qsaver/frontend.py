from __future__ import unicode_literals

import pykka 

from mopidy.core import CoreListener

class QSaverFrontend(pykka.ThreadingActor, CoreListener):
	def __init__(self, config, core):
		super(QSaverFrontend, self).__init__()
        self.config = config
        self.core = core

    def saveQueue():
    	# TODO: save the queue to a local file
    	logger.info("Qsaver is saving the tracklist");

    def restoreQueue():
    	# TODO: restore the queue from a local file 
    	logger.info("Qsaver is restoring your tracklist");

    def on_start(self):
        self.restoreQueue()

    def on_stop(self):
        self.saveQueue()

    def track_playback_started(self, tl_track):
    	self.saveQueue()
