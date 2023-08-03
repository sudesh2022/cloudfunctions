# cloudfunctions
login to ibmcloud login --sso select the appropriate org target the appropriate resource 
ibmcloud target -g sudesh-resource 
target the function project : ibmcloud ce project select -n watsonx-functions 
< For new ones Create a repo in git clone it to your local system add a folder inside> 
1) build the python file make sure u have requirements.txt for the import statement .
1a) The function should work on your machine. Otherwise you have to debug and fix on your machine before you create a cloud function 
2) push all the changes try and run the function 
3) ibmcloud ce fn create -n telljoke -runtime python-3.11 --build-source github_url 
4) You can either curl <url> OR see on cloud dashboard 
5) if there are any issues you have to use the debug of the function