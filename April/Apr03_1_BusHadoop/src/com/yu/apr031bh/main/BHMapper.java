package com.yu.apr031bh.main;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// IN
//		2022,01,01,1호선,서울역,5,1
//			or
//		2022,01,01,100번(하계동~용산구청),한성여객종점,3,1
// OUT
//		겨울,4

// 겨울이 날짜 수가 적어서(2월은 28일까지밖에)
// 여름이 날짜 수가 많고(7,8월이 연속으로 31일까지)
//	=> 단순 합계 내면 겨울이 손해
//	=> 데이터 수로 나눠서 평균을 내는 걸로
public class BHMapper extends Mapper<Object, Text, Text, DoubleWritable> {
	private static final Text SEASON = new Text();
	private static final DoubleWritable PASSENGER = new DoubleWritable();
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		String[] str = value.toString().split(",");
		if (Integer.parseInt(str[1]) >= 3 && Integer.parseInt(str[1]) <= 5) {
			SEASON.set("봄");
		} else if (Integer.parseInt(str[1]) >= 6 && Integer.parseInt(str[1]) <= 8) {
			SEASON.set("여름");
		} else if (Integer.parseInt(str[1]) >= 9 && Integer.parseInt(str[1]) <= 11) {
			SEASON.set("가을");
		} else {
			SEASON.set("겨울");
		}
		PASSENGER.set(Double.parseDouble(str[5]) + Double.parseDouble(str[6]));
		context.write(SEASON, PASSENGER);
	}
}
