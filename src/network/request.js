import axios from 'axios'

export function request(config) {
  const instance = axios.create({
    baseURL: 'http://119.8.160.160:5000',
    timeout: 5000
  })

  instance.interceptors.request.use(config => {
    return config
  }, err => {
    console.log(err);
  })

  instance.interceptors.response.use(res => {
    return res.data
  }, err => {
    console.log(err)
  })

  return instance(config)
}
