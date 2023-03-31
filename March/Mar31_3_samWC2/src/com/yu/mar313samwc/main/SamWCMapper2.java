package com.yu.mar313samwc.main;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// 관우가 많이 죽였나, 장비가 많이 죽였나

// 베다, 베고, 베었다, 벤 후, 벨 때, 베어 넘기고, ... ? #1
// 이런 거 처리하려면 -> 자연어처리/형태소분석 어쩌구

// Java로 하고 있는 hadoop : 전처리는 내가 맡는다[완전 쓸데없는 데이터만 걷어내는 정도]
//		대용량 데이터 상대 좋음
//		분석 자체는 약함
//		=> 전처리나 하자 == 용량을 줄이자 -> 그럼 더 이상 대용량이 아니니

// Python으로 하게 될 Numpy, Pandas, ... BD/AI관련 lib 잘 돼 있음
//		분석 자체는 여기가 더 편함
//		대용량은 감당 불가
//		=> 줄여온 데이터를 본격적으로 분석함

// 따라서, 이번에 #1 처리는 못 하고 <- 이건 Python에게 넘김
// 관우나 장비가 등장하는 문장 정도만 결과로 내주자
public class SamWCMapper2 extends Mapper<Object, Text, Text, IntWritable> {
	private static final IntWritable ONE = new IntWritable(1);
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		String line = value.toString();
		if (line.contains("관우") || line.contains("장비")) {
			context.write(value, ONE);
		}
	}
}
