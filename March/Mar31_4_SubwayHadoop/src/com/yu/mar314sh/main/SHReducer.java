package com.yu.mar314sh.main;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

//combine 단계
//-------------
//		1호선 84200, 20000

//reduce 단계
//------------
//		1호선 104200

// IntWritable -> LongWritable
public class SHReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
	private static final LongWritable PASSENGER_RESULT = new LongWritable();
	@Override
	protected void reduce(Text arg0, Iterable<LongWritable> arg1,
			Reducer<Text, LongWritable, Text, LongWritable>.Context arg2) throws IOException, InterruptedException {
		long sum = 0;
		for (LongWritable obj : arg1) {
			sum += obj.get();
		}
		PASSENGER_RESULT.set(sum);
		arg2.write(arg0, PASSENGER_RESULT);
	}
}
