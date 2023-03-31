package com.yu.mar314sh.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// map 단계
//---------
// IN
//		2015,01,01,1호선,서울역,47071,40197
//		2015,01,01,1호선,시청역,11016,8943
// OUT
//		1호선 84200
//		1호선 20000

// combine 단계
//-------------
//		1호선 84200, 20000

// reduce 단계
//------------
//		1호선 104200

// 단순히 크기비교
// 냅다 합계 -> 2호선이 제일 큰데 -> 2호선이 제일 많다
// 생긴지 얼마 안 된 노선은?, 이것도 제대로 분석하려면 평균 내야 함
public class SHMain {
	public static void main(String[] args) {
		try {
			Configuration c = new Configuration();
			Job j = Job.getInstance(c);
			j.setMapperClass(SHMapper.class);
			j.setCombinerClass(SHReducer.class);
			j.setReducerClass(SHReducer.class);
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(LongWritable.class);
			// 어차피 map 오버라이딩 구조상 /subway.csv에 밖에 못 쓰는데 그냥 하드코딩
			FileInputFormat.addInputPath(j, new Path("/subway.csv"));
			
			// 지금은 노선별로 하는데
			// 나중에 역별로 할 수도 있으니
			FileOutputFormat.setOutputPath(j, new Path(args[0]));
			// bin/hadoop jar subway.jar 결과폴더경로 <- 이 경우엔, 이렇게 쓰면 실행 됨
			j.waitForCompletion(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
