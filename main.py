from kivy.core.audio import SoundLoader
from kivy.utils import platform
from kivy.logger import Logger
import time


class MusicPlayerAndroid(object):
    def __init__(self):

        from jnius import autoclass
        media_player = autoclass('android.media.MediaPlayer')
        self.mplayer = media_player()

        self.secs = 0
        self.actualsong = ''
        self.length = 0
        self.isplaying = False

    def __del__(self):
        self.stop()
        self.mplayer.release()
        Logger.info('mplayer: deleted')

    def load(self, filename):
        try:
            self.actualsong = filename
            self.secs = 0
            self.mplayer.setDataSource(filename)
            self.mplayer.prepare()
            self.length = self.mplayer.getDuration() / 1000
<<<<<<< HEAD
            Logger.info('mplayer load: %s' % filename)
            Logger.info('type: %s' % type(filename))
=======
            Logger.info('mplayer load: %s' %filename)
            Logger.info('type: %s' %type(filename))
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e
            return True
        except:
            Logger.info('error in title: %s' % filename)
            return False

    def unload(self):
        self.mplayer.reset()

    def play(self):
        self.mplayer.start()
        self.isplaying = True
        Logger.info('mplayer: play')

    def stop(self):
        self.mplayer.stop()
        self.secs = 0
        self.isplaying = False
        Logger.info('mplayer: stop')

    def seek(self, timepos_secs):
        self.mplayer.seekTo(timepos_secs * 1000)
<<<<<<< HEAD
        Logger.info('mplayer: seek %s' % int(timepos_secs))

    def pause(self):
        try:
            self.mplayer.pause()
        except:
            Logger.info('Internal player engine has not been initialized.')
=======
        Logger.info('mplayer: seek %s' %int(timepos_secs))
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e


class MusicPlayerWindows(object):
    def __init__(self):
        self.secs = 0
        self.actualsong = ''
        self.length = 0
        self.isplaying = False
        self.sound = None

    def __del__(self):
        if self.sound:
            self.sound.unload()
            Logger.info('mplayer: deleted')

    def load(self, filename):
        self.__init__()
        # if type(filename) == unicode: filename = filename.encode('utf-8')   # unicode does not work !
        self.sound = SoundLoader.load(filename)
        if self.sound:
            if self.sound.length != -1:
                self.length = self.sound.length
                self.actualsong = filename
<<<<<<< HEAD
                Logger.info('mplayer: load %s' % filename)
                return True
            else:
                Logger.info('mplayer: songlength = -1 ...')
        return False

    def unload(self):
        if self.sound is not None:
            self.sound.unload()
            self.__init__  # reset vars
=======
                Logger.info('mplayer: load %s' %filename)
                return True
            else:
                Logger.info ('mplayer: songlength = -1 ...')
        return False

    def unload(self):
        if self.sound != None:
            self.sound.unload()
            self.__init__   # reset vars
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e

    def play(self):
        if self.sound:
            self.sound.play()
            self.isplaying = True
            Logger.info('mplayer: play')

    def stop(self):
        self.isplaying = False
<<<<<<< HEAD
        self.secs = 0
=======
        self.secs=0
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e
        if self.sound:
            self.sound.stop()
            Logger.info('mplayer: stop')

    def seek(self, timepos_secs):
        self.sound.seek(timepos_secs)
<<<<<<< HEAD
        Logger.info('mplayer: seek %s' % int(timepos_secs))
=======
        Logger.info('mplayer: seek %s' %int(timepos_secs))
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e


def main():
    songs = [
        # 'f:\\_mp3_\\_testdir_\\file of ☠☢☣.mp3',    # insert songs here
        'D:\\Muzyka\\AC DC\\Iron Man 2 (Soundtrack)\\01. Shoot To Thrill.mp3'
        # 'f:\\_mp3_\\Patricks Mp3s\\electro\\Echotek - Freak Africa.mp3',
        # 'f:\\_mp3_diverse_\\Testsuite\\flac\\01 - Jam & Spoon - Stella (Jam & Spoon Mix).flac',
        # 'f:\\_mp3_\\P1\\1Start\\Hot Chip - boy from school.mp4'
<<<<<<< HEAD
    ]

    Logger.info('platform: %s' % platform)

    mplayer = ''
=======
        ]

    Logger.info('platform: %s' %platform)

>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e
    if platform == 'win':
        mplayer = MusicPlayerWindows()
    elif platform == 'android':
        mplayer = MusicPlayerAndroid()
    else:
        exit()

    for s in songs:
<<<<<<< HEAD
        if mplayer.load(s):  # checking load, seek
            mplayer.play()
            time.sleep(10)
            # mplayer.pause()
            # time.sleep(10)
            # mplayer.play()
            # time.sleep(10)
            # mplayer.seek(90)
            # time.sleep(2)
=======
        if mplayer.load(s):     # checking load, seek
            mplayer.play()
            time.sleep(2)
            mplayer.seek(90)
            time.sleep(2)
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e
            mplayer.stop()
            mplayer.unload()

        else:
<<<<<<< HEAD
            Logger.info('cant load song: %s' % s)
=======
            Logger.info('cant load song: %s' %s)
>>>>>>> ec4605d083e18fca70b727a5d1ed1744b4a0276e


if __name__ == '__main__':
    main()
