import caffe
import numpy as np
import cv2
import Image
import os

#nvcamerasrc
#gst = "/dev/video1 ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)I420 ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"

#gst-launch-1.0 v4l2src device="/dev/video1" ! 'video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420, framerate=(fraction)30/1' ! nvvidconv flip-method=0 ! 'video/x-raw, format=(string)I420' ! videoconvert ! 'video/x-raw, format=(string)BGR' ! fakesink

MODEL_FILE='/home/nvidia/colordata/deploy.prototxt'
WEIGHT_CAFFEMODEL='/home/nvidia/colordata/snapshot_iter_4480.caffemodel'
MEAN_FILE='/home/nvidia/colordata/mean.npy'
LABEL='/home/nvidia/colordata/post_label.txt'

caffe.set_mode_gpu()
caffe.set_device(0)


def main():

	cap = cv2.VideoCapture(1)

	net = caffe.Net(MODEL_FILE,WEIGHT_CAFFEMODEL,caffe.TEST)

	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_mean('data', np.load(MEAN_FILE).mean(1).mean(1))

	transformer.set_transpose('data', (2,0,1))
	transformer.set_channel_swap('data', (2,1,0)) # if using RGB instead of BGR
	transformer.set_raw_scale('data', 255.0)

	net.blobs['data'].reshape(1,3,224,224)
	count=1
	res='start'
	os.system("bash init.sh") #initialize gpio pins

	while(True):
   	 # Capture frame-by-frame
		count += 1
		ret, frame = cap.read()
		cv2.putText(frame,res,(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
		cv2.imshow('frame',frame)
		
		if res=="blue":
			os.system("bash blue.sh")  #script to switch on blue and switch offf rest
		elif res == "green":
			os.system("bash green.sh")
		elif res == "orange":
			os.system("bash orange.sh")
		elif res == "red":
			os.system("bash red.sh")


		if count % 5 == 0:        #process every 5th frame
			cv2.imwrite('temp.png', frame)
			img = caffe.io.load_image('temp.png') #/media/anilsathyan7/work/imdb/47/tomato-109.jpg
			net.blobs['data'].data[...] = transformer.preprocess('data', img)

			output = net.forward()

			output_prob = output['softmax'][0]
			print output['softmax'].argmax()


			label_mapping = np.loadtxt(LABEL, str, delimiter='\t')
			best_n = net.blobs['softmax'].data[0].flatten().argsort()[-1:-6:-1]

			top_inds = output_prob.argsort()[::-1][:5]  # reverse sort and take five largest items
			res = label_mapping[top_inds][0][1]
			print "It looks like a ",label_mapping[top_inds][0][1]

		if cv2.waitKey(1) & 0xFF == ord('q'):
        		break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
