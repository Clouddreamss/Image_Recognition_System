<template>
    <el-main>
        <el-table
            :data="
                tableData.filter(
                    (data) =>
                        !search ||
                        data.name.toLowerCase().includes(search.toLowerCase())
                )
            "
            style="width: 100%"
            @selection-change="handleSelectionChange"
        >
            <el-table-column type="selection" width="55"> </el-table-column>
            <el-table-column label="板件id" prop="id"> </el-table-column>
            <el-table-column label="清洗时间" prop="date"> </el-table-column>
            <el-table-column label="清洗率" prop="rate"> </el-table-column>
            <el-table-column label="清洗情况" prop="status"> </el-table-column>
            <el-table-column align="right">
                <template slot="header" slot-scope="{}">
                    <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入关键字搜索"
                    />
                </template>
                <template slot-scope="scope">
                    <el-button
                        size="mini"
                        @click="handleEdit(scope.$index, scope.row)"
                        >查看</el-button
                    >
                    <el-button
                        size="mini"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)"
                        >Delete</el-button
                    >
                </template>
            </el-table-column>
        </el-table>
        <!-- 弹窗区域 -->
        <el-dialog title="查看" :visible.sync="dialogVisible" width="75%">
            <el-row :gutter="20">
                <el-col :span="8">
                    <el-card class="image-card">
                        <img
                            src="../../../../src/picture/originPic.jpg"
                            alt="清洗前"
                            class="image"
                        />
                        <div class="detectedDes">识别前</div>
                    </el-card>
                </el-col>
                <!-- 识别后图片及数据展示 -->
                <el-col :span="8">
                    <el-card class="image-card">
                        <img
                            src="../../../../src/picture/detected.jpg"
                            alt="识别后"
                            class="image"
                        />
                        <div class="detectedDes">识别后</div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card>
                        <span class="color-rate">颜色覆盖率:</span>
                        <span class="color-data">102.395583333333%</span>
                    </el-card>
                </el-col>
            </el-row>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="reWash()">处理</el-button>
            </div>
        </el-dialog>
    </el-main>
</template>


<script>
export default {
    data() {
        return {
            tableData: [
                {
                    id: '001',
                    date: '2016-05-02',
                    status: '合格',
                    rate: '100%'
                },
                {
                    id: '001',
                    date: '2016-05-03',
                    status: '合格',
                    rate: '100%'
                },
                {
                    id: '001',
                    date: '2016-05-04',
                    status: '不合格',
                    rate: '80%'
                },
                {
                    id: '001',
                    date: '2016-05-05',
                    status: '合格',
                    rate: '100%'
                }
            ],
            search: '',
            dialogVisible: false
        }
    },
    methods: {
        handleSelectionChange(val) {
            this.multipleSelection = val
        },
        //查看弹窗
        handleEdit(index, row) {
            console.log(index, row)
            this.dialogVisible = true
            console.log('dia', this.dialogVisible)
        },
        handleDelete(index, row) {
            console.log(index, row)
        },
        reWash() {
            this.$confirm('确认重新清洗该件?')
                .then((_) => {
                    this.dialogVisible = false
                })
                .catch((_) => {})
        }
    }
}
</script>

<style scoped>
.el-row {
    display: flex;
    flex-wrap: wrap;
}
.image-card {
    height: 100%;
    min-width: 100%;
}
.image {
    height: 300px;
}
.color-rate {
    font-size: 20px;
}
.color-data {
    display: block;
    color: rgb(3, 195, 131);
    font-size: 18px;
}
.detectedDes {
    text-align: center;
    margin-top: 10px;
    font-size: 16px;
}
</style>