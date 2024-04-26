def recommend(user_skin_type, df, similarity_matrix, top=10):
    products = []
    try:
        index = df[df['skintype'] == user_skin_type].index[0]
        distances = sorted(enumerate(similarity_matrix[index]), reverse=True, key=lambda x: x[1])
        for i in distances[1:top+1]:
            products.append({ "name": df.iloc[i[0]]['name'], "type": df.iloc[i[0]]['type'] })
        return products
    except IndexError:
        return products