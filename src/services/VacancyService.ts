import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IVacancy } from '../modules/IVacancy'
import camelcaseKeys from 'camelcase-keys'

const vacancyApi = createApi({
    reducerPath: 'vacancyApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://localhost:3000/vacancies',
        prepareHeaders: (headers) => {
            headers.set('Content-Type', 'application/json')
            headers.set('Authorization', `Bearer ${localStorage.getItem('accessToken')}`)
            return headers
        }
    }),
    endpoints: (build) => ({
        getVacancies: build.query<IVacancy[], number>({
            query: (limit: number = 10) => ({
                url: '/',
                params: {
                    limit
                }
            }),
            transformResponse: (response: IVacancy[]) => camelcaseKeys(response, { deep: true })
        }),
        getVacancy: build.query<IVacancy[], string>({
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