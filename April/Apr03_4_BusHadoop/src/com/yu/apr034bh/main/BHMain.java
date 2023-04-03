package com.yu.apr034bh.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// 2022,01,01,100번(하계동~용산구청),한성여객종점,300,100

// 100번(하계동~용산구청) 400 - x <- 이번엔 합계 아님
// 100번(하계동~용산구청) 300 - o <- 탄 사람
// 100번(하계동~용산구청) 100 - o <- 내린 사람
// 탄거 내린거 따로 나갈 수 있게

// hadoop 결과 : 키\t값\r\n
public class BHMain {
	public static void main(String[] args) {
		try {
			Job j = Job.getInstance(new Configuration());
			j.setMapperClass(BHMapper.class);
			j.setCombinerClass(BHReducer.class);
			j.setReducerClass(BHReducer.class);
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(LongWritable.class);
			FileInputFormat.addInputPath(j, new Path("/bus2021.csv"));
			FileInputFormat.addInputPath(j, new Path("/bus2022.csv"));
			FileOutputFormat.setOutputPath(j, new Path(args[0]));
			j.waitForCompletion(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
