from flask import Flask, request, render_template, jsonify
from firebase_admin import credentials, firestore, initialize_app
# Initialize Flask App
app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')

currentSpot= 1
emailAddress=None
name=None
startImage=[]
for i in range(7):
    startImage.append("/static/img/transparent.png")
feedbackValue=[]
for i in range(7):
    feedbackValue.append(0)

@app.route('/')
def home():
    global currentSpot
    global emailAddress
    global startImage
    global feedbackValue
    global name
    currentSpot= 1
    emailAddress=None
    name=None
    startImage=[]
    for i in range(7):
        startImage.append("/static/img/transparent.png")
    startImage[6]="/static/img/finalImage.png"
    startImage[0]="/static/img/robotimage.png"
    feedbackValue=[]
    for i in range(7):
        feedbackValue.append(0)
    todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
               
    return render_template('home.html' )

@app.route('/add', methods=['POST','GET'])
def create():
    global currentSpot
    global emailAddress
    global startImage
    global feedbackValue
    global name
    todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
    
    if request.method == 'POST':
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            import re
            if not(re.fullmatch(regex, request.form['emailaddress'])):
                return render_template('home.html', message="Enter a valid email address!" )
            if not request.form['name']:
                return render_template('home.html', message="Enter a name!" )
            currentSpot= 1
            emailAddress=None
            name=None
            startImage=[]
            for i in range(7):
                startImage.append("/static/img/transparent.png")
            startImage[6]="/static/img/finalImage.png"
            startImage[0]="/static/img/robotimage.png"
            feedbackValue=[]
            for i in range(7):
                feedbackValue.append(0)
            emailAddress=request.form['emailaddress']
            name=request.form['name']
            for doc in todo_ref.stream():
                docdict=doc.to_dict()
                if (docdict['email']==emailAddress):
                    currentSpot=docdict['currentSpot']
                    name=docdict['name']
                    feedbackValue=docdict['feedbackValues']
                    break
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            
            for i in range(7):
                startImage[i] = "/static/img/transparent.png"
            startImage[6]="/static/img/finalImage.png"
            startImage[currentSpot-1] = "/static/img/robotimage.png"
                    
            todo_ref.document(emailAddress).set({'email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            return render_template('interaction.html', startImage2=startImage, feedbackValue2=feedbackValue, name2=name, emailaddress2=emailAddress)
    for i in range(7):
                startImage[i] = "/static/img/transparent.png"
    startImage[6]="/static/img/finalImage.png"
    startImage[currentSpot-1] = "/static/img/robotimage.png"
    return render_template('home.html' )


@app.route('/nextState')
def nextState():
            global currentSpot
            global emailAddress
            global feedbackValue
            global name
            global startImage
            for doc in todo_ref.stream():
                docdict=doc.to_dict()
                if 'type' in docdict.keys():
                    currentSpot=docdict['currentSpot']
                    name=docdict['name']
                    feedbackValue=docdict['feedbackValues']
                    emailAddress=docdict['email']
                    break
            if currentSpot+1 <=7:
                currentSpot+=1
            for i in range(7):
                startImage[i] = "/static/img/transparent.png"
            startImage[6]="/static/img/finalImage.png"
            startImage[currentSpot-1] = "/static/img/robotimage.png"
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            # todo_ref.document(emailAddress).set({'email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            return render_template('interaction.html', startImage2=startImage, feedbackValue2=feedbackValue, name2=name, emailaddress2=emailAddress)
        
        
@app.route('/previousState')
def previousState():
            global currentSpot
            global emailAddress
            global feedbackValue
            global startImage
            global name
            for doc in todo_ref.stream():
                docdict=doc.to_dict()
                if 'type' in docdict.keys():
                    currentSpot=docdict['currentSpot']
                    name=docdict['name']
                    feedbackValue=docdict['feedbackValues']
                    emailAddress=docdict['email']
                    break
            if currentSpot-1>=1:
                currentSpot-=1
            for i in range(7):
                startImage[i] = "/static/img/transparent.png"
            startImage[6]="/static/img/finalImage.png"
            startImage[currentSpot-1] = "/static/img/robotimage.png"
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            # todo_ref.document(emailAddress).set({'email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            return render_template('interaction.html', startImage2=startImage, feedbackValue2=feedbackValue, name2=name, emailaddress2=emailAddress)
                
        
@app.route('/feedbackAdd')
def feedbackAdd():
            global currentSpot
            global emailAddress
            global startImage
            global feedbackValue
            global name
            for doc in todo_ref.stream():
                docdict=doc.to_dict()
                if 'type' in docdict.keys():
                    currentSpot=docdict['currentSpot']
                    name=docdict['name']
                    feedbackValue=docdict['feedbackValues']
                    emailAddress=docdict['email']
                    break
            for i in range(7):
                startImage[i] = "/static/img/transparent.png"
            startImage[6]="/static/img/finalImage.png"
            startImage[currentSpot-1] = "/static/img/robotimage.png"
            feedbackValue[currentSpot-1] +=1
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})

            # todo_ref.document(emailAddress).set({'email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            return render_template('interaction.html', startImage2=startImage, feedbackValue2=feedbackValue, name2=name, emailaddress2=emailAddress)
                        
        
@app.route('/feedbackMinus')
def feedbackMinus():
            global currentSpot
            global emailAddress
            global startImage
            global feedbackValue
            global name
            for doc in todo_ref.stream():
                docdict=doc.to_dict()
                if 'type' in docdict.keys():
                    currentSpot=docdict['currentSpot']
                    name=docdict['name']
                    feedbackValue=docdict['feedbackValues']
                    emailAddress=docdict['email']
                    break
            feedbackValue[currentSpot-1] -=1
            for i in range(7):
                startImage[i] = "/static/img/transparent.png"
            startImage[6]="/static/img/finalImage.png"
            startImage[currentSpot-1] = "/static/img/robotimage.png"
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            # todo_ref.document(emailAddress).set({'email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            return render_template('interaction.html', startImage2=startImage, feedbackValue2=feedbackValue, name2=name, emailaddress2=emailAddress)
                        
@app.route('/Submit')
def Submit():
            global currentSpot
            global emailAddress
            global startImage
            global feedbackValue
            global name
            for doc in todo_ref.stream():
                docdict=doc.to_dict()
                if 'type' in docdict.keys():
                    currentSpot=docdict['currentSpot']
                    name=docdict['name']
                    feedbackValue=docdict['feedbackValues']
                    emailAddress=docdict['email']
                    break
            
            for i in range(7):
                startImage[i] = "/static/img/transparent.png"
            startImage[6]="/static/img/finalImage.png"
            startImage[currentSpot-1] = "/static/img/robotimage.png"
            todo_ref.document("Current Data").set({'type': 'current','email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            todo_ref.document(emailAddress).set({'email':emailAddress,'name':name, 'currentSpot':currentSpot, 'feedbackValues':feedbackValue})
            return render_template('finalPage.html', startImage2=startImage, feedbackValue2=feedbackValue, name2=name, emailaddress2=emailAddress)      
