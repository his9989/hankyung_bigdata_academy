#실행하고 싶은 명령어에 커서두고 F5 누르면 실행.
#	#은 주석
#	$은 필터? 설정할때

setwd("c:/R_data")	# 폴더 셋팅
dir()				# 세팅 폴더 리스트 보여줌

txt<-read.csv("치킨선호도조사.csv", header=T)	# 치킨선호도조사 파일 읽어내는 파일
							# header=T는 필터 제목을넣는 것(F는 뺌)
							# txt<- : scv 파일을 txt에 넣음
							#  여기서 txt는 그냥 변수!(a같은거)
str(txt)		# 이 txt파일의 구조를 파악
names(txt)

summary(txt)	# 결과를 정리해주는 기능

txt[2, ]		# 여기 4개는 통계(집계) 내줌
txt[, 2]
txt[2]
txt$성별

집계.성별<-table(txt$성별)
집계.성별
barplot(집계.성별)	# 바 그래프로 결과 보여주는 기능

집계.지역<-table(txt$지역)
집계.지역
barplot(집계.지역)

##########################################
#단, data가 오직 숫자로 존재하는 경우만 사용 가능
#문자가 끼어있는 경우에는 문자를 제거해야함

mtcars		#기본 함수
summary(mtcars)
table(mtcars$gear)

plot(mtcars$mpg)		# 산포도 보여주는 명령어
plot(mtcars$wt)

plot(mtcars$disp, mtcars$hp)	# x축이 disp, y축이 hp인 경우 상관관계 보여주는 기능
cor(mtcars$disp, mtcars$hp)		# 그래프 기울기를 알려주는 기능

cor(mtcars)				# 각 변수끼리의 기울기를 모두 계산해주는 기능
plot(mtcars)				# 각 변수끼리 상관관계 그래프를 모두 보여주는 기능

boxplot(mtcars)		#평균값 기준으로 위, 아래 표시
				#특이 순간이 발생한경우 동그라미로 표시.(무슨 사건이 있을 가능성 있음)

#########################################
