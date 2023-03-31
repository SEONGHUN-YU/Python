package com.yu.mar312samwc.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// 삼국지연의 소설책
//		실제역사 : 조조가 주인공
//		저 소설 : 유비를 중심으로
//		어쨌든 3국지 인데?
//		=> 조조, 유비, 손권 언급횟수 세보기

//	한글은 조사 때문에 제대로 세기 어려움
//		한글처리 : hadoop은 한글처리 필요없고 utf-8이면 됨

//	분석용 데이터 파일은 꼭 utf-8로!

//	csv가 MS Excel에서 열리는데
//	MS Excel이 utf-8을 못 알아봄
//	그럼에도 불구하고 utf-8을 고집했던 이유는 hadoop 때문임

// 자동완성 하고 치울 녀석들 넣기
//		common
//		mapreduce-client-core
public class SamWCMain {
	public static void main(String[] args) {
		try {
			Configuration c = new Configuration();
			Job j = Job.getInstance(c);
			
			j.setMapperClass(SamWCMapper.class);
			j.setCombinerClass(SamWCReducer.class);
			j.setReducerClass(SamWCReducer.class);
			
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(IntWritable.class);
			
			// 아까 그거는 단순히 단어 수 세는 거
			// => 딱 sherlock만 세는 건가?
			// => 다른 것도 단어 수 셀 때 써먹자
			// FileInputFormat.addInputPath(j, new Path("/sherlock.txt"));
			// => FileInputFormat.addInputPath(j, new Path(args[0]));
			
			// 조조, 유비, 손권 : 삼국지에나 나오지
			// => 이 프로그램은 삼국지에서밖에 못 씀
			// => 삼국지가 10권인데
			String title = null;
			for (int i = 1; i <= 10; i++) {
				title = String.format("/sam%02d.txt", i);
				FileInputFormat.addInputPath(j, new Path(title));
			}
			FileOutputFormat.setOutputPath(j, new Path("/samResult"));
			j.waitForCompletion(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
