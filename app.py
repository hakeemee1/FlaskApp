from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   # เช็คเงื่อนไขให้ Name ที่กรอกมาตรงตามที่กำหนด
   if name == 'Hakeemee':
      return '<h2>welcome %s</h2>' % name
   else: 
      return '<h2>sorry %s, login is failed</h2>' % name


# Route ไปยัง form เพื่อที่จะรับค่า Post ที่ได้มา

@app.route('/login',methods = ['POST', 'GET']) 
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user)) 
      # เรียกใช้ฟังก์ชั่น success เเละส่ง parameter 'nm' ไปยังฟังก์ชัน
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host='0.0.0.0',port='5000',debug=True)