package com.yu.mar312samwc.main;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// IN
//		유비가 조조를 만나 향후를 논의했다
//		조조는 반갑게 맞이했다
//		손권은 아니고
// OUT
//		유비 1
//		조조 1
//		조조 1
//		유비 1
//		손권 1 <- 이게 목표
public class SamWCMapper extends Mapper<Object, Text, Text, IntWritable> {
	private static final Text WHO = new Text();
	private static final IntWritable ONE = new IntWritable(1);
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		// 그 단어에 유비/조조/손권이 포함되면 <- 이게 필요
		StringTokenizer st = new StringTokenizer(value.toString(), " ");
		String word = null;
		while (st.hasMoreElements()) {
			word = st.nextToken();
			// 맹덕, 조승상 처리는 어떡하게?
			if (word.contains("조조") || word.contains("맹덕")) {
				WHO.set("조조");
			} else if (word.contains("유비") || word.contains("현덕")) {
				WHO.set("유비");
			} else if (word.contains("손권") || word.contains("중모")) {
				WHO.set("손권");
			} else {
				continue;
			}
			context.write(WHO, ONE);
		}
	}
}
