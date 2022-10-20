  index=np.where(pt.index==userinput)[0][0]
#     similaritems=sorted(list(enumerate(similarityscore[index])),key=lambda x:x[1] ,reverse=True)[1:6]

#     data=[]

#     for i in  similaritems:
#         item=[]
# #         print(i[0]) to print names only
# #         print(pt.index[i[0]]) but we want title and other info too
#         tempdf=books[books['Book-Title']==pt.index[0]]
#     #as with different isbn same three books name come so remove that
#         item.extend(list(tempdf.drop_duplicates('Book-Title')['Book-Title'].values))
#         item.extend(list(tempdf.drop_duplicates('Book-Title')['Book-Author'].values))
#         item.extend(list(tempdf.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
#         data.append(item)
#         print(data)