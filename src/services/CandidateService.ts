import camelcaseKeys from 'camelcase-keys'
import baseApi from './BaseApi'
import { ICandidateProm, ICandidatesResponseData, INewCandidate } from '../modules/ICandidate'
import decamelizeKeys from 'decamelize-keys'

const candidateApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        fetchVacancyCandidates: build.query<ICandidatesResponseData, {limit: number, id: string}>({
            query: ({limit = 10, id}) => ({
                url: `/api-c-p/?vacancy_id=${id}`,
                params: {
                    limit
                }
            }),
            transformResponse: (response: any): ICandidatesResponseData => camelcaseKeys(response, { deep: true })
        }),
        fetchVacancyAllCandidates: build.query<ICandidatesResponseData, string>({
            query: (id) => ({
                url: `/api-c-p/?vacancy_id=${id}`,
            }),
            transformResponse: (response: any): ICandidatesResponseData => camelcaseKeys(response, { deep: true })
        }),
        fetchAllCandidates: build.query<ICandidatesResponseData, void>({
            query: () => ({
                url: `/api-c-p/`,
            }),
            transformResponse: (response: any): ICandidatesResponseData => camelcaseKeys(response, { deep: true }),
            providesTags: result => ['Candidate']
        }),
        fetchCandidates: build.query<ICandidatesResponseData, string>({
            query: (params) => ({
                url: `/api-c-p/${params}`,
            }),
            transformResponse: (response: any): ICandidatesResponseData => camelcaseKeys(response, { deep: true })
        }),
        fetchCandidate: build.query<ICandidateProm, string>({
            query: (id) => ({
                url: `/api-c-p/${id}/`,
            }),
            transformResponse: (response: any): ICandidateProm => camelcaseKeys(response, { deep: true })
        }),
        createCandidate: build.mutation<INewCandidate, INewCandidate>({
            query: (candidate) => ({
                url: `/api-new-cand/`,
                method: 'POST',
                body: JSON.stringify(decamelizeKeys(candidate))
            }),
            invalidatesTags: ['Candidate']
        })
    })
})

export default candidateApi