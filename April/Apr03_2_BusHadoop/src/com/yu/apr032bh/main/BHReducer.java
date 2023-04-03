package com.yu.apr032bh.main;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class BHReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	private static final DoubleWritable PASSENGER_AVG = new DoubleWritable();
	@Override
	protected void reduce(Text arg0, Iterable<DoubleWritable> arg1,
			Reducer<Text, DoubleWritable, Text, DoubleWritable>.Context arg2) throws IOException, InterruptedException {
		long sum = 0, count = 0;
		for (DoubleWritable obj : arg1) {
			sum += obj.get();
			count++;
		}
		PASSENGER_AVG.set(sum / (double) count);
		arg2.write(arg0, PASSENGER_AVG);
	}
}
