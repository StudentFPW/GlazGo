import { PayloadAction, createSlice } from "@reduxjs/toolkit";
import { IPagination } from "../../modules/IPagination";

const initialState: IPagination = {
    count: 0,
    previous: '',
    next: '',
    params: '',
    startCount: 0,
    endCount: 0,
}

const paginationSlice = createSlice({
    name: 'pagination',
    initialState,
    reducers: {
        setPaginationData(state, action: PayloadAction<IPagination>) {
            state.count = action.payload.count
            state.previous = action.payload.previous ? action.payload.previous.slice(action.payload.previous.indexOf('?')) : ''
            state.next = action.payload.next ? action.payload.next.slice(action.payload.next.indexOf('?')) : ''
            state.startCount = action.payload.previous ? state.startCount + 10 : 1
            if (action.payload.count < 10) {
                state.endCount = action.payload.count
            } else if (action.payload.count > 10) {
                if (state.next) {
                    state.endCount = 10
                } else {
                    state.endCount = action.payload.count
                }
            }
        },
        setParams(state, payload: PayloadAction<string>) {
            state.params = payload.payload
        },
    }
})

export const {setPaginationData, setParams} = paginationSlice.actions

export default paginationSlice.reducer