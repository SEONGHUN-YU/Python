package com.yu.mar312samwc.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

// IN
//		조조 1,1,1,1,1,1,1,1
// OUT
//		조조 8

// 단어 수 세는 게 아니고, 평균 내는 거라면? 못 함 <- Python에서 처리해야 함
// hadoop만으로 모든 걸 끝낼 수는 없음
// 3TB -> 30MB -> Python에서 처리 <- 이게 hadoop의 존재 이유, 어디까지나 전처리용
public class SamWCReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
	private static final IntWritable SUM = new IntWritable();
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException {
		int sum = 0;
		for (IntWritable obj : arg1) {
			sum += obj.get();
		}
		SUM.set(sum);
		arg2.write(arg0, SUM);
	}
}
