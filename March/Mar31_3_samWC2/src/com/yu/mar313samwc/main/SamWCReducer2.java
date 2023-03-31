package com.yu.mar313samwc.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class SamWCReducer2 extends Reducer<Text, IntWritable, Text, IntWritable> {
	private static final IntWritable ONE = new IntWritable(1);
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException {
		arg2.write(arg0, ONE);
	}
}
