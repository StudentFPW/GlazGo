import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IVacancy, IVacancyResponseData } from '../modules/IVacancy'
import camelcaseKeys from 'camelcase-keys'

const vacancyApi = createApi({
    reducerPath: 'vacancyApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://127.0.0.1:8000',
        prepareHeaders: (headers) => {
            headers.set('Content-Type', 'application/json')
            headers.set('Authorization', `Bearer ${localStorage.getItem('accessToken')}`)
            return headers
        }
    }),
    endpoints: (build) => ({
        fetchVacancies: build.query<IVacancyResponseData, number>({
            query: (limit: number = 10) => ({
                url: '/api-vac/',
                params: {
                    limit
                }
            }),
            transformResponse: (response: any): IVacancyResponseData => camelcaseKeys(response, { deep: true })
        }),
        fetchVacancy: build.query<IVacancy[], string>({
            query: (id) => ({
                url: '/',
                params: {
                    id
                }
            }),
            transformResponse: (response: IVacancy[]) => camelcaseKeys(response, { deep: true })
        })
    })
})

export default vacancyApi