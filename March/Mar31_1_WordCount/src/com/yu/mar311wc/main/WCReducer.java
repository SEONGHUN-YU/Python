package com.yu.mar311wc.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

// hadoop 작업 2단계 : combine
// 자동으로 처리되니 존재감 제로

// IN
//		how 1
//		are 1
//		you 1
//		you 1
//		are 1
//		good 1
// OUT
//		how 1
//		are 1,1
//		you 1,1
//		good 1

// -------------------------------------------

// hadoop 작업 3단계 : reduce
//	합계내는 작업을 함

// IN
//		how 1
//		are 1,1
//		you 1,1
//		good 1
// OUT
//		how 1
//		are 2
//		you 2
//		good 1

// Mapper 쪽의 KEYOUT, VALUEOUT과 Reducer쪽의 KEYIN, VALUEIN이 일치해야 함
public class WCReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
	
	// int -> IntWritable로 바꾸고 싶을 뿐인데
	// 굳이 객체를 만들게 되면 메모리가... 그래서 이런 식으로 처리하는 것
	private static final IntWritable SUM = new IntWritable();
	
	// combine된 거 한 덩어리마다 불러짐(you 1,1 <- 이런 게 한 덩어리)
	@Override
	protected void reduce(Text arg0, // you
			Iterable<IntWritable> arg1, // 1,1
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) // 결과처리용도
			throws IOException, InterruptedException {
		
		int sum = 0;
		for (IntWritable iw : arg1) {
			// IntWritable -> int로 바꿔주는 method
			sum += iw.get();
		}
		
		SUM.set(sum);
		arg2.write(arg0, SUM);
	}
}
