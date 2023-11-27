import camelcaseKeys from 'camelcase-keys'
import baseApi from './BaseApi'
import { ICandidateProm } from '../modules/ICandidate'

export interface ICandidatesResponseData {
    results: ICandidateProm[]
}

const candidateApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        fetchCandidates: build.query<ICandidatesResponseData, {limit: number, id: string}>({
            query: ({limit = 10, id}) => ({
                url: `/api-c-p/?vacancy_id=${id}`,
                params: {
                    limit
                }
            }),
            transformResponse: (response: any): ICandidatesResponseData => camelcaseKeys(response, { deep: true })
        }),
        fetchCandidate: build.query<ICandidateProm, string>({
            query: (id) => ({
                url: `/api-c-p/${id}/`,
            }),
            transformResponse: (response: any): ICandidateProm => camelcaseKeys(response, { deep: true })
        })
    })
})

export default candidateApi