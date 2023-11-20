import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IVacancyItem } from '../modules/IVacancyItem'

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
        getVacancies: build.query<IVacancyItem[], number>({
            query: (limit: number = 10) => ({
                url: '/',
                params: {
                    limit
                }
            })
        }),
        getVacancy: build.query<IVacancyItem, string>({
            query: (id) => ({
                url: '/',
                params: {
                    id
                }
            })
        })
    })
})

export default vacancyApi