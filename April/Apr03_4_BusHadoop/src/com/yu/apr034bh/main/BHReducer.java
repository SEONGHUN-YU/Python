package com.yu.apr034bh.main;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class BHReducer extends Reducer<Text, LongWritable, Text, LongWritable>{
	private static final LongWritable SUM = new LongWritable(); 
	@Override
	protected void reduce(Text arg0, Iterable<LongWritable> arg1,
			Reducer<Text, LongWritable, Text, LongWritable>.Context arg2) throws IOException, InterruptedException {
		long sum = 0;
		for (LongWritable obj : arg1) { // 어차피 (_타)때도 호출하고
			sum += obj.get();			// (_내)때도 호출하기 때문에 전부 구해서 보내짐
		}
		SUM.set(sum);
		arg2.write(arg0, SUM);
	}
}
