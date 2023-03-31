package com.yu.mar313samwc.main;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class SamWCMain2 {
	public static void main(String[] args) {
		try {
			Configuration c = new Configuration();
			Job j = Job.getInstance(c);
			j.setMapperClass(SamWCMapper2.class);
			j.setCombinerClass(SamWCReducer2.class);
			j.setReducerClass(SamWCReducer2.class);
			j.setOutputKeyClass(Text.class);
			j.setOutputValueClass(IntWritable.class);
			String title = null;
			for (int i = 1; i <= 10; i++) {
				title = String.format("/sam%02d.txt", i);
				FileInputFormat.addInputPath(j, new Path(title));
			}
			FileOutputFormat.setOutputPath(j, new Path("/samResult2"));
			j.waitForCompletion(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
