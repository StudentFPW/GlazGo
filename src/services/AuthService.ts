import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IAuthData } from '../modules/IAuth'
import { IRegQueryData, IRegResponseData } from '../modules/IReg'
import decamelizeKeys from 'decamelize-keys'

const authApi = createApi({
    reducerPath: 'authApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://127.0.0.1:8000',
        prepareHeaders: (headers) => {
            headers.set('Content-Type', 'application/json')
            return headers
        },
        // credentials: 'include'
    }),
    endpoints: (build) => ({
        registration: build.mutation<IRegResponseData, IRegQueryData>({
            query: (regData) => ({
                url: '/auth/reg/',
                method: 'POST',
                body: JSON.stringify(decamelizeKeys(regData))
            })
        }),
        login: build.mutation<IRegResponseData, IAuthData>({
            query: (authData) => ({
                url: '/auth/login/',
                method: 'POST',
                body: JSON.stringify(authData)
            })
        }),
        logout: build.mutation({
            query: () => ({
                url: '/auth/logout/',
                method: 'POST',
                credentials: 'include'
            })
        }),
        checkAuth: build.mutation({
            query: () => ({
                url: '/auth/token/refresh/',
                method: 'POST',
                // credentials: 'include'
            })
        })
    })
})

export default authApi