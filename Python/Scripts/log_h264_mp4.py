import logging, sys, time, cv2, ffmpeg, numpy

logger = logging.getLogger("Writer")
logger.setLevel("INFO")
formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(module)s %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
videoCapture = cv2.VideoCapture('/home/servadmin/Downloads/motion-11-55-41.avi')
process = (
    ffmpeg
    .input('pipe:', framerate='{}'.format(videoCapture.get(cv2.CAP_PROP_FPS)), format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    .output('output/out.mp4', vcodec='h264_v4l2m2m', pix_fmt='nv21', **{'b:v': 2000000})
    .overwrite_output()
    .run_async(pipe_stdin=True)
)
lastFrame = False
frames = 0
start = time.time()
while not lastFrame:
    ret, image = videoCapture.read()
    if ret:
        process.stdin.write(
            image
            .astype(numpy.uint8)
            .tobytes()
        )        
        frames += 1
    else:
        lastFrame = True
elapsed = time.time() - start
logger.info("%d frames" % frames)
logger.info("%4.1f FPS, elapsed time: %4.2f seconds" % (frames / elapsed, elapsed))
del videoCapture
