package com.yu.mar314sh.main;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// 아까 : 비정형데이터 소설책(.txt)
// 이번 : 정형데이터 (.csv)

//map 단계
//---------
//IN
//		2015,01,01,1호선,서울역,47071,40197
//		2015,01,01,1호선,시청역,11016,8943
//OUT
//		1호선 84200
//		1호선 20000
public class SHMapper extends Mapper<Object, Text, Text, LongWritable> {
	private static final Text SUBWAY_LINE = new Text();
	private static final LongWritable PASSENGER = new LongWritable();
	protected void map(Object key, Text value, Mapper<Object, Text, Text, LongWritable>.Context context)
			throws IOException, InterruptedException {
		
		String[] str = value.toString().split(",");
		SUBWAY_LINE.set(str[3]);
		PASSENGER.set(Long.parseLong(str[5]) + Long.parseLong(str[6]));
		context.write(SUBWAY_LINE, PASSENGER);
		
		// 정형데이터 : 2015,01,01,1호선,서울역,47071,40197
		// 		,로 나눠서 4번째 거에 접근해서...
		//		특정 위치에 접근하기 편함
		//		=> 배열로 만들어주는 split이 유리(무조건이란 소리 아니다)
		
		// 비정형데이터 : 낙양 북쪽 천3백 리에 자리잡고 있는 평원군은
		//		화이트스페이스로 나눠서 5번째 거에 접근? 불가능
		//		=> while문 돌리기 편한 StringTokenizer가 유리(무조건이란 소리 아니다)
	}
}
