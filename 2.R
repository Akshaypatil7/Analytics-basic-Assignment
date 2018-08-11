rm(list=ls())

#a.	Load CSV in R by skipping second row
Df=read.csv("IMDB_data.csv",header=T,stringsAsFactors=F,sep=",")[-2,]

#b.	Extract the unique genres and its count and store in data frame with index key. 
unique_genres=unique(Df$'Genre')
unique_length=length(unique_genres)
Index_Key=c(1:unique_length)
w=table(Df$Genre)
t=as.data.frame(w)
p=t[-1,]
DF_Genres<-data.frame(Index_Key,p)
D_Genres=data.frame(Index=DF_Genres$Index_Key,DF_Genres$Var1,DF_Genres$Freq)
#c.	Convert the required data types
Df$imdbRating=as.numeric(Df$imdbRating)
Df$Year=as.numeric(Df$Year)
Df$imdbVotes=as.numeric(Df$imdbVotes)
Df$Genre=as.factor(Df$Genre)
Df$Language=as.factor(Df$Language)
str(Df)
#d.	Sort the genre by its name
Df=Df[order(Df$Genre),]
#e.	Create new variable whose values should be square of difference between imdbrating and imdbvotes.
Df$squared_difference_btwn_imdbrating_imdbvotes=with(Df,(imdbRating-imdbVotes)^2)
