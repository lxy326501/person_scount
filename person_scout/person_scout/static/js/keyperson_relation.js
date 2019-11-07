	// 人物关系
	var dom = document.getElementById("relation");
	var relation = echarts.init(dom);
	var app = {};
	relation_option = null;
	relation_option = {
		tooltip: {},
		animationDurationUpdate: 1500,
		animationEasingUpdate: 'quinticInOut',
		series : [
			{
				type: 'graph',
				layout: 'none',
				symbolSize: 50,
				roam: true,
				label: {
					normal: {
						show: true
					}
				},
				color:["#ff9b53"],
				edgeSymbol: ['circle', 'arrow'],
				edgeSymbolSize: [4, 10],
				edgeLabel: {
					normal: {
						textStyle: {
							fontSize: 20
						}
					}
				},
				data: [{
					name: '用户1',
					x: 300,
					y: 300
				}, {
					name: '用户2',
					x: 800,
					y: 300
				}, {
					name: '用户3',
					x: 550,
					y: 100
				}, {
					name: '用户4',
					x: 550,
					y: 500
				}],
				// links: [],
				links: [{
					source: 0,
					target: 1,
					symbolSize: [5, 20],
					lineStyle: {
						normal: {
							width: 5,
							curveness: 0.2
						}
					}
				}, {
					source: '用户2',
					target: '用户1',
					lineStyle: {
						normal: { curveness: 0.2 }
					}
				}, {
					source: '用户1',
					target: '用户3'
				}, {
					source: '用户2',
					target: '用户3'
				}, {
					source: '用户2',
					target: '用户4'
				}, {
					source: '用户1',
					target: '用户4'
				}],
				lineStyle: {
					normal: {
						opacity: 0.9,
						width: 2,
						curveness: 0
					}
				}
			}
		]
	};;
	if (relation_option && typeof relation_option === "object") {
		relation.setOption(relation_option, true);
	}