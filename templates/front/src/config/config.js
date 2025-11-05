export default {
	baseUrl: 'http://localhost:8080/django85gv12pu/',
	name: '/django85gv12pu',
	indexNav: [
		{
			name: '商品信息',
			url: '/index/shangpinxinxi',
		},
		{
			name: '留言信息',
			url: '/index/forum'
		}, 
		{
			name: '公告资讯',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '留言信息',
			refTable: 'forumtype',
			refColumn: 'typename',
		},
		{
			name: '公告资讯',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
