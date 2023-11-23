import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IAuthData } from '../modules/IAuth'
import { IRegData } from '../modules/IReg'
import decamelizeKeys from 'decamelize-keys'
import { ITokens } from '../modules/ITokens'

const userApi = createApi({
    reducerPath: 'userApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://127.0.0.1:8000',
        prepareHeaders: (headers) => {
            headers.set('Content-Type', 'application/json')
            return headers
        }
    }),
    endpoints: (build) => ({
        fetchReg: build.mutation<ITokens, IRegData>({
            query: (regData) => ({
                url: '/auth/reg/',
                method: 'POST',
                body: JSON.stringify(decamelizeKeys(regData))
            })
        }),
        fetchAuth: build.mutation<ITokens, IAuthData>({
            query: (authData) => ({
                url: '/auth/login/',
                method: 'POST',
                body: JSON.stringify(authData)
            })
        })
    })
})

export default userApi