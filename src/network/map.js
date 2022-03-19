import axios from 'axios'

export function getMapData() {
  const instance = axios.create({
    baseURL: 'https://d209m3w127yzkd.cloudfront.net/data/calcAggOutput.js',
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