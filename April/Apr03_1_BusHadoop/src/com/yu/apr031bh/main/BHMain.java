package com.yu.apr031bh.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// 보유기술목록에
//		kxml???
//		json-simple???
//		Hadoop은 괜찮네

// Spring framework : 기술이라고 해도 되나?
// Hadoop
// Numpy
// kxml.jar
// beautifulsoup4.py
public class BHMain {
	public static void main(String[] args) {
		try {
			// MC CC RC OK OV, FIF FOF wFC
			Job j = Job.getInstance(new Configuration());
			j.setMapperClass(BHMapper.class);
			j.setCombinerClass(BHReducer.class);
			j.setReducerClass(BHReducer.class);
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(DoubleWritable.class);
			FileInputFormat.addInputPath(j, new Path("/bus2015.csv"));
			// HDFS에 /bus2015.csv가 있어야 실행 됨
			// FIF에 2개 이상 쓸 경우 띄어쓰기 없는 ,로 연결된 명령어의 모습이 됨
			FileInputFormat.addInputPath(j, new Path("/bus2016.csv"));
			FileOutputFormat.setOutputPath(j, new Path(args[0]));
			j.waitForCompletion(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
