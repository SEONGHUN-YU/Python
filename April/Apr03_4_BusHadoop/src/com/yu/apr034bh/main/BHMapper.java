package com.yu.apr034bh.main;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class BHMapper extends Mapper<Object, Text, Text, LongWritable> {
	private static final Text NO_ON = new Text();
	private static final Text NO_OFF = new Text();
	private static final LongWritable ON = new LongWritable();
	private static final LongWritable OFF = new LongWritable();
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, LongWritable>.Context context)
			throws IOException, InterruptedException {
		String[] str = value.toString().split(",");
		NO_ON.set(str[4] + "_타");
		NO_OFF.set(str[4] + "_내");
		ON.set(Long.parseLong(str[5]));
		OFF.set(Long.parseLong(str[6]));
		context.write(NO_ON, ON); // 정류장_타 300
		context.write(NO_OFF, OFF); // 정류장_내 100 이런식으로 감
	}
}
