// JavaScript Document

// 人物画像-词云
	var chart = echarts.init(document.getElementById('word_cloud'));
	
	var word_cloud = {
		tooltip: {},
		title:{
			text:"用户关键词",
			x:"50",
			textStyle:{
				color:"#666"
			}
		},
		series: [ {
			type: 'wordCloud',
			gridSize: 2,
			sizeRange: [14, 50],
			rotationRange: [-90, 90],
			shape: 'pentagon',
			width: 600,
			height: 150,
			drawOutOfBound: true,
			textStyle: {
				normal: {
					color: function () {
						return 'rgb(' + [
							Math.round(Math.random() * 160),
							Math.round(Math.random() * 160),
							Math.round(Math.random() * 160)
						].join(',') + ')';
					}
				},
				emphasis: {
					shadowBlur: 5,
					shadowColor: '#333'
				}
			},
			data: [
				{
					name: 'Sam S Club',
					value: 10000,
					textStyle: {
						normal: {
							color: 'black'
						},
						emphasis: {
							color: 'red'
						}
					}
				},
				{
					name: 'Macys',
					value: 6181
				},
				{
					name: 'Amy Schumer',
					value: 4386
				},
				{
					name: 'Jurassic World',
					value: 4055
				},
				{
					name: 'Charter Communications',
					value: 2467
				},
				{
					name: 'Chick Fil A',
					value: 2244
				},
				{
					name: 'Planet Fitness',
					value: 1898
				},
				{
					name: 'Pitch Perfect',
					value: 1484
				},
				{
					name: 'Express',
					value: 1112
				},
				{
					name: 'Home',
					value: 965
				},
				{
					name: 'Johnny Depp',
					value: 847
				},
				{
					name: 'Lena Dunham',
					value: 582
				},
				{
					name: 'Lewis Hamilton',
					value: 555
				},
				{
					name: 'KXAN',
					value: 550
				},
				{
					name: 'Mary Ellen Mark',
					value: 462
				},
				{
					name: 'Farrah Abraham',
					value: 366
				},
				{
					name: 'Rita Ora',
					value: 360
				},
				{
					name: 'Serena Williams',
					value: 282
				},
				{
					name: 'NCAA baseball tournament',
					value: 273
				},
				{
					name: 'Point Break',
					value: 265
				}
			]
		} ]
	};
	
	chart.setOption(word_cloud);
	
	// 人物画像-饼状图
	var dom = document.getElementById("tweets_category");
	var tweets_category = echarts.init(dom);
	tweets_category_option = null;
	tweets_category_option = {
		title : {
			text: '推文类别占比',
			x:'50',
			textStyle:{
				color:"#666"
			}
		},
		tooltip : {
			trigger: 'item',
			formatter: "{a} <br/>{b} : {c} ({d}%)"
		},
		color:['#24dbef','#319ee6','#ffb077','#40d6ae'],
		series: [
			{
				name:'访问来源',
				type:'pie',
				radius: ['50%', '70%'],
				center: ['50%', '55%'],
				label: {
				},
				data:[
					{value:335, name:'黄'},
					{value:215, name:'赌'},
					{value:164, name:'毒'},
					{value:236, name:'政'},
				],
				itemStyle: {
					borderWidth: 1,
					borderColor: '#fff' 
				  },
			}
		]
	};
	if (tweets_category_option && typeof tweets_category_option === "object") {
		tweets_category.setOption(tweets_category_option, true);
	}
	
	// 人物画像-热力图
	var dom = document.getElementById("thermodynamic_chart");
	var thermodynamic_chart = echarts.init(dom);
	var app = {};
	option = null;
	
	var hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a',
			'7a', '8a', '9a','10a','11a',
			'12p', '1p', '2p', '3p', '4p', '5p',
			'6p', '7p', '8p', '9p', '10p', '11p'];
	var days = ['黄', '赌', '毒',
			'政'];
	
	var data = [[0,0,5],[0,1,1],[0,2,0],[0,3,0],[0,4,0],[0,5,0],[0,6,0],[0,7,0],[0,8,0],[0,9,0],[0,10,0],[0,11,2],[0,12,4],[0,13,1],[0,14,1],[0,15,3],[0,16,4],[0,17,6],[0,18,4],[0,19,4],[0,20,3],[0,21,3],[0,22,2],[0,23,5],[1,0,7],[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0],[1,6,0],[1,7,0],[1,8,0],[1,9,0],[1,10,5],[1,11,2],[1,12,2],[1,13,6],[1,14,9],[1,15,11],[1,16,6],[1,17,7],[1,18,8],[1,19,12],[1,20,5],[1,21,5],[1,22,7],[1,23,2],[2,0,1],[2,1,1],[2,2,0],[2,3,0],[2,4,0],[2,5,0],[2,6,0],[2,7,0],[2,8,0],[2,9,0],[2,10,3],[2,11,2],[2,12,1],[2,13,9],[2,14,8],[2,15,10],[2,16,6],[2,17,5],[2,18,5],[2,19,5],[2,20,7],[2,21,4],[2,22,2],[2,23,4],[3,0,7],[3,1,3],[3,2,0],[3,3,0],[3,4,0],[3,5,0],[3,6,0],[3,7,0],[3,8,1],[3,9,0],[3,10,5],[3,11,4],[3,12,7],[3,13,14],[3,14,13],[3,15,12],[3,16,9],[3,17,5],[3,18,5],[3,19,10],[3,20,6],[3,21,4],[3,22,4],[3,23,1]];
	
	option = {
		tooltip: {
			position: 'top'
		},
		title: [],
		color:['#24dbef','#319ee6','#ffb077','#40d6ae'],
		singleAxis: [],
		series: []
	};
	
	echarts.util.each(days, function (day, idx) {
		option.title.push({
			textBaseline: 'middle',
			top: (idx + 0.5) * 100 / 4 + '%',
			text: day
		});
		option.singleAxis.push({
			left: 150,
			type: 'category',
			boundaryGap: false,
			data: hours,
			top: (idx * 100 / 4 + 5) + '%',
			height: (100 / 4 - 10) + '%',
			axisLabel: {
				interval: 2
			},
			nameTextStyle:{
				color:"0000ff"
			},
			axisLine:{
				textStyle:{
					color:"0000ff"
				},
				lineStyle:{
					color:'#aaa'
				}
			}
		});
		option.series.push({
			singleAxisIndex: idx,
			coordinateSystem: 'singleAxis',
			type: 'scatter',
			data: [],
			symbolSize: function (dataItem) {
				return dataItem[1] * 4;
			}
		});
	});
	
	echarts.util.each(data, function (dataItem) {
		option.series[dataItem[0]].data.push([dataItem[1], dataItem[2]]);
	});;
	if (option && typeof option === "object") {
		thermodynamic_chart.setOption(option, true);
	}
