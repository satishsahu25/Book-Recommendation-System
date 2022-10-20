from flask import Flask, render_template,request
import pickle
import numpy as np

populardf=pickle.load(open('populardfmod.pkl','rb'))
# rb--read binary mode
pt=pickle.load(open('pt.pkl','rb'))
similarityscore=pickle.load(open('similarityscore.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))


app=Flask(__name__)

@app.route("/")
def hello_world():
    # return 'Hello worlss'
    return render_template('index.html',
        bookname=list(populardf['Book-Title'].values),
        author=list(populardf['Book-Author'].values),
        image=list(populardf['Image-URL-M'].values),
        votes=list(populardf['NumRating'].values),
        rating=list(populardf['AvgRating'].values)
    )

@app.route('/recommended')
def recommededui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommedbooks():
    userinput=request.form.get('userinput')
    index=np.where(pt.index==userinput)[0][0]
    similaritems=sorted(list(enumerate(similarityscore[index])), key=lambda x:x[1] ,reverse=True)[1:6]

    data=[]

    for i in  similaritems:
        item=[]
        tempdf=books[books['Book-Title']==pt.index[i[0]]]
        item.extend(list(tempdf.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(tempdf.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(tempdf.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
        print(data)
 
    return render_template('recommend.html',data=data)

if __name__=='__main__':
    # app.run(debug=True,port=8000)
    app.run(debug=True)