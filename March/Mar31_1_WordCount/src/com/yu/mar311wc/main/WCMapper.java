package com.yu.mar311wc.main;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// hadoop 작업 1단계 : map
// 이 단계에서는 합산은 안 함

// IN
//		how are you
//		you are good
// OUT
//		how 1
//		are 1
//		you 1
//		you 1
//		are 1
//		good 1

// sherlock.txt 소설을 넣을 거
// csv, txt 들을 자주할텐데, 첫 번째 자리는 쓸 일이 거의 없을 것 <- Object로 퉁치기

// Mapper의 generic에 쓸 게 없어도 안 쓰면 안 되니 Object로 얼버무려 놓자
public class WCMapper 
	extends Mapper<Object, Text, // 뭐가 들어오는지 <?, 텍스트>
					Text, IntWritable>{ // 뭐가 나가는지 <텍스트, 출현횟수> (hadoop 버전 자료형을 썼다고 보면 됨)
	// 단순히 String -> Text가 하고싶은 건데
	// 반복문속에서 Text객체를 계속 만들면 -> 컴 폭발
	// 그래서 여기다 멤버변수로 만듬
	private static final Text WORD = new Text();
	private static final IntWritable ONE = new IntWritable(1);
	
	// 이 method가 한 문장마다 불러짐
	@Override
	protected void map(
			Object key, // 딱히 의미가 없음...(값이 있나없나 확인하는 정도로만 씀)
			Text value, // 그 문장 내용(how are you ... 같은 거) 
			Mapper<Object, Text, Text, IntWritable>.Context context) // 결과처리용도
			throws IOException, InterruptedException {
		
		// Text -> String
		String line = value.toString();
		// split or StringTokenizer(비정형은 이게 더 어울림)
		StringTokenizer st = new StringTokenizer(line, " ");
		
		while(st.hasMoreElements()) {
			WORD.set(st.nextToken()); // 위에 만들어놓은 WORD에다가 내용만 바꿔서
			context.write(WORD, ONE); // 다음단계로 보내기(즉, 결과처리 하는 애)
		}
	}
}
