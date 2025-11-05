const base = {
    get() {
        return {
            url : "http://localhost:8080/django85gv12pu/",
            name: "django85gv12pu",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于DJANGO框架的多功能校园网站的设计与实现"
        } 
    }
}
export default base
