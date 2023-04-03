package com.yu.apr032bh.main;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// 빅데이터 과정 : Python으로 끝내자(샘플데이터만 쓰니)

// 대부분의 데이터에 요일은 없음 => 요일은 구해서 써야 함
// 대용량데이터 요일 Python으로 구하면 => ... 참담함
//		서버급 컴 여러대로 구해야 함
public class BHMapper extends Mapper<Object, Text, Text, DoubleWritable> {
	private static final Text DAY = new Text();
	private static final DoubleWritable PASSENGER = new DoubleWritable();
	private static final SimpleDateFormat S_TO_D = new SimpleDateFormat("yyyyMMdd");
	private static final SimpleDateFormat D_TO_S = new SimpleDateFormat("E");
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		try {
			String[] str = value.toString().split(",");
			Date day = S_TO_D.parse(str[0] + str[1] + str[2]);
			String day_str = D_TO_S.format(day);
			DAY.set(day_str);
			PASSENGER.set(Double.parseDouble(str[5]) + Double.parseDouble(str[6]));
			context.write(DAY, PASSENGER);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
