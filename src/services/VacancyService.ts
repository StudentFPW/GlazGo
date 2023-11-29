import { IVacancy, IVacancyResponseData } from '../modules/IVacancy'
import camelcaseKeys from 'camelcase-keys'
import baseApi from './BaseApi'
import decamelizeKeys from 'decamelize-keys'

const vacancyApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        fetchAllVacancies: build.query<IVacancyResponseData, void>({
            query: () => ({
                url: '/api-vac/',
            }),
            transformResponse: (response: any): IVacancyResponseData => camelcaseKeys(response, { deep: true })
        }),
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
        }),
        createVacancy: build.mutation<IVacancy, IVacancy>({
            query: (vacancy) => ({
                url: `/api-vac/`,
                method: 'POST',
                body: JSON.stringify(decamelizeKeys(vacancy))
            })
        })
    })
})

export default vacancyApi