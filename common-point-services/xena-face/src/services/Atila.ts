import { NuxtAxiosInstance } from '@nuxtjs/axios'

type Message = {
  id: string
  from: string | null
  to: string | null
  subject: string
  content: string
  replyTo: string | null
  replies: Message[]
}

class Atila {
  public readonly axios: NuxtAxiosInstance

  constructor (axios?: NuxtAxiosInstance) {
    this.axios = axios
  }

  public getCount = (axios: NuxtAxiosInstance) => {
    return axios({
      method: 'GET',
      url: `${process.env.XENA_ATILA_HOST}/clients/stats/count`,
    })
    .catch(err => console.warn(err))
    .then(resp => {
      if (resp)
        return resp.data as number[]
    })
  }

  public getClients = (axios: NuxtAxiosInstance) => {
    return axios({
      method: 'GET',
      url: `${process.env.XENA_ATILA_HOST}/clients`,
    })
    .catch(err => console.warn(err))
    .then(resp => {
      if (resp)
        return resp.data
    })
  }

  public fetchMessages = (axios: NuxtAxiosInstance, clientId: string, withReplies?: boolean) => {
    return axios({
      method: 'GET',
      url: `${process.env.XENA_ATILA_HOST}/messages`,
      params: {
        clientId,
        withReplies,
      }
    })
    .catch(err => console.warn(err))
    .then(resp => {
      if (resp)
        return resp.data as Message[]
    })
  }

  public publishMessage = (axios: NuxtAxiosInstance, clientId: string, subject: string, content: string) => {
    return axios({
      method: 'POST',
      url: `${process.env.XENA_ATILA_HOST}/messages`,
      data: {
        to: clientId,
        subject,
        content,
      },
    })
    .catch(err => console.warn(err))
    .then(resp => {
      if (resp)
        return resp.data
    })
  }
}

export default new Atila()