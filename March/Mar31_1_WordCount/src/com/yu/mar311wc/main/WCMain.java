package com.yu.mar311wc.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// Hadoop : Linux * n로 병렬처리하는 Java프로그램
// 굳이 Linux에서 vi로 할 필요있나
// MS Windows에서 IDE로 만들어서 => 실행만 Linux에서
// Windows에서는 실행해봐야 에러남

// Windows에서 Eclipse를 쓰는 이유 : 자동완성 쓰려고 <- 사실 이거..
// 어차피 여기서 실행해봐야 에러남

// Linux에는 hadoop 설치 다 해놨음
// 우리는 저 많은 것들 중에 Windows에서 쓸 자동완성에 필요한 것만 가져올 것
// 정식 maven 할 필요없고 그냥 다운 받아서 쓰자

// hadoop은 따로 한글처리 필요없고 그냥 utf-8이기만 하면 다 된다

//		hadoop-common
//		hadoop-mapreduce-client-core

// hadoop은 작업이 3단계로 나눠짐
// map단계
// combine단계 - 자동으로 처리 됨, 사실 그래서 거의 없는 취급 당함(사람이 신경 안 씀)
// reduce단계
// 각 단계별로 class를 만들어야 함

// sherlock.txt 단어 수 세기 <- 오늘 목표
public class WCMain {
	public static void main(String[] args) {
		try {
			Configuration c = new Configuration();
			Job j = Job.getInstance(c);
			
			j.setMapperClass(WCMapper.class);
			j.setCombinerClass(WCReducer.class);
			j.setReducerClass(WCReducer.class);
			
			// Reducer쪽의 KEYOUT, VALUEOUT과 일치해야 함
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(IntWritable.class);
			
			// hadoop은 DB에 있는 거 분석을 못 함
			// HDFS에 있는 거만 분석할 줄 앎
			// DB에 있는 거 -> csv로 바꾸는 이유가 hadoop이 저 모양이라서임...

			// FileInputFormat.addInputPath(j, new Path("/sherlock.txt"));
			// 이런식으로 적으면 sherlock만 분석 가능
			// 실행명령어쓸 때 sherlock.txt을 써서 분석하게 만들면 더 좋잖아(soft coding으로)
			
			// 실행명령어	분석대상	결과저장할 경로 <- cmd에서 이런 식으로 쓰게될 것
			FileInputFormat.addInputPath(j, new Path(args[0])); // 패키지명 긴 걸로
			FileOutputFormat.setOutputPath(j, new Path(args[1])); // 패키지명 긴 걸로
			
			j.waitForCompletion(true); // 분석 끝날 때까지 가만히 있게 만듬
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
