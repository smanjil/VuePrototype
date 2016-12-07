
new Vue({

    el: '#root',

    data: {
        username: '',
        password: ''
    },

    methods: {
        checkLogin(){
            var uname = this.username;
            var pass = this.password;

            axios.post('/login',{
                'username': uname,
                'password': pass
            }).then((response) => {
                console.log(response.status);
            });
        }
    }

});
