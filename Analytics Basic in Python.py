
#a.Load CSV in Python by skipping second row.
import pandas as pd
import numpy as np
df=pd.read_csv('IMDB_data.csv',sep=',',encoding='iso-8859-1',skiprows=[2])

#b.Extract the unique genres and its count and store in data frame with index key. 
genre_count=df['Genre'].value_counts().rename_axis('uniquegenres').reset_index(name='Counts')
genre_index=pd.DataFrame({'index key':range(len(genre_count))})
genre_count_with_index=pd.concat([genre_index.reset_index(drop=True),genre_count],axis=1)

#c.Convert the required data types
df.imdbVotes=df.imdbVotes.replace('-',0).fillna(0).astype(int)
df.imdbRating=df.imdbRating.replace('-',0).astype(float)
df.Genre=df.Genre.astype('category')
df.Language=df.Language.astype('category')
df.Plot=df.Plot.str.split(',').astype(str)
df.Year=pd.to_numeric(df.Year,errors='coerce')
df.imdbID=df.imdbID.astype(str)

#d.	Sort the genre by its name
df=df.sort_values('Genre',ascending=True)

#e.	Create new variable whose values should be square of difference between imdbrating and imdbvotes.
s=df.imdbRating-df.imdbVotes
df['squared_difference_btwn_imdbrating_imdbvotes']=np.square(s)



