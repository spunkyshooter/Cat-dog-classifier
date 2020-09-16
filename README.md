
First instructions before executing python file.

1. First make ensure the package requirements are satisfied.
   To install the requirements execute the command below

   pip install -r requirements.txt

2. For Training execute DNN.py file as shown below

	python3 DNN.py

	while Training, A learning rate graph will be plotted.
	Program halts there, close the window, then it continues

3. For Testing execute test.py file as shown below

	python3 test.py

	For testing, you can give any image. 
	just put the name of the image inside the test.py file. open the file, you get the idea where to write it.
	For testing the accuracy we need to know the ground truth value, just for comparision, hence
	write 1 if its a cat and 0 if its non-cat inside the file. 
	
