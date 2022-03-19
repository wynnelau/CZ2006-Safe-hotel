import axios from 'axios'

export function getHotelData() {
  const instance = axios.create({
    baseURL: 'http://localhost:8080/public/ceshi.json',
    timeout: 5000
  })

  var config = {
    url: "",
    method: "get"
  }

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