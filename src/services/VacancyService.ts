import { IVacancy, IVacancyResponseData } from '../modules/IVacancy'
import camelcaseKeys from 'camelcase-keys'
import baseApi from './BaseApi'

const vacancyApi = baseApi.injectEndpoints({
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
        fetchVacancy: build.query<IVacancy, string>({
            query: (id) => ({
                url: `/api-vac/${id}/`,
            }),
            transformResponse: (response: any): IVacancy => camelcaseKeys(response, { deep: true })
        })
    })
})

export default vacancyApi